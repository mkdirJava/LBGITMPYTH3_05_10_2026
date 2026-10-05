import difflib

with open("bank.master") as f:
    master = f.readlines()

with open("bank.out") as f:
    current = f.readlines()

if master == current:
    print("PASS: No differences found")
else:
    print("FAIL: Differences detected\n")

    diff = difflib.unified_diff(
        master,
        current,
        fromfile="bank.master",
        tofile="bank.out"
    )

    print("".join(diff))

    # Alternative Output
    Hdiff = difflib.HtmlDiff().make_table(master, current)
    open("differences.html", "w").writelines(Hdiff)
