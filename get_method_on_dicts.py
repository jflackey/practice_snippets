name_for_userid = {
    1: "John",
    2: "Sam",
    3: "Alfred",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(1))
# "Hi John!"

print(greeting(4))
# "Hi there!"
