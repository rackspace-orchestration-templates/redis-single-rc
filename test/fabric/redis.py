from fabric.api import env, task
from envassert import detect, file, group, port, process, service, user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    assert file.exists("/etc/redis/redis.conf")
    assert port.is_listening(6379)
    assert user.exists("redis")
    assert group.is_exists("redis")
    assert process.is_up("redis-server")
    assert service.is_enabled("redisredis")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
