def main():
    msg = input()

    result = convert(msg)

    print(result)

def convert(msg):
    msg1 = msg.replace(":)", '\N{slightly smiling face}')

    msg2 = msg1.replace(":(", '\N{slightly frowning face}')

    return msg2

main()