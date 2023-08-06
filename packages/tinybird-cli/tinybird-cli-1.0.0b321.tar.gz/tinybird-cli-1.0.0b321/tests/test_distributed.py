from uuid import uuid4
from tornado.testing import AsyncTestCase
import tornado
from tests_e2e.aux import poll_async
from tinybird.async_redis import async_redis_writer
from tinybird.redis_client import TBRedisConfigDirect, get_redis_args
from tinybird.distributed import WorkingGroup


class TestDistributed(AsyncTestCase):
    @tornado.testing.gen_test
    async def test_workinggroup(self):
        redis_args = get_redis_args()
        redis_config = TBRedisConfigDirect(
            host=redis_args.get('host'),
            port=redis_args.get('port', None),
            db=redis_args.get('db')
        )
        async_redis_writer.init(redis_config)
        workinggroup_id = f"test_wg_{uuid4()}"
        wg1 = await WorkingGroup(workinggroup_id, 'worker1', ttl=1, keepalive_interval=0.1).init()
        assert wg1.score_index('k0') == 0
        wg2 = await WorkingGroup(workinggroup_id, 'worker2', ttl=1, keepalive_interval=0.1).init()

        async def f():
            assert {wg1.score_index('k0'), wg2.score_index('k0')} == {0, 1}

        await poll_async(f)

        if wg1.score_index('k0') == 1:
            wg1, wg2 = wg2, wg1
        # wg1 has lower priority, closing wg2 to check priority changes (as wg1 disappears)
        await wg2.exit()

        async def f2():
            assert wg1.score_index('k0') == 0
            assert len(wg1._workers) == 1

        await poll_async(f2)

        await wg1.exit()
        await async_redis_writer.close()
