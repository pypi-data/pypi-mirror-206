import env

assert env.get("TOKEN") == "abc123"
assert env.get("X", None) is None
assert env.get_int("PORT") == 123
assert env.get_strs("KEYS", []) == ["word1", "F402", "12"]
assert env.get_ints("ADMIN_IDS") == [1, 2, 3]
assert env.get_ints("X", [0]) == [0]

with env.prefix("BOOL"):
    assert env.get_bool("T")
    assert not env.get_bool("F")

try:
    env.get("X")
except Exception as e:
    assert str(e) == 'Mandatory environment variable "X" is missing'

try:
    env.get_ints("BAD_NUMS")
except Exception as e:
    assert str(e) == 'Failed to cast "1,2,a" (variable name "BAD_NUMS") to list'

try:
    env.get_bool("BAD_BOOL")
except Exception as e:
    assert str(e) == 'Failed to cast "ok" (variable name "BAD_BOOL") to bool'

assert env.raw.float("FLOAT") == 1.45
