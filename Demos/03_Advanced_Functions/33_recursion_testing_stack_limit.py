def call_me_again_from_within(n):
    n += 1
    print(n)
    call_me_again_from_within(n)

call_me_again_from_within(0)
