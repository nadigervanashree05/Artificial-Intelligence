
# Forward Chaining in First Order Logic

# Initial Knowledge Base (Facts)
facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Owns", "A", "T1"),
    ("Missile", "T1")
}

# Forward Chaining Algorithm
def forward_chaining(facts):

    while True:
        new_facts = set()

        # Rule 1: Missile(x) -> Weapon(x)
        for fact in facts:
            if fact[0] == "Missile":
                new_facts.add(("Weapon", fact[1]))

        # Rule 2: Missile(x) AND Owns(A,x)
        #         -> Sells(Robert,x,A)
        for f1 in facts:
            for f2 in facts:
                if (f1[0] == "Missile" and
                    f2[0] == "Owns" and
                    f2[1] == "A" and
                    f1[1] == f2[2]):

                    new_facts.add(
                        ("Sells", "Robert", f1[1], "A")
                    )

        # Rule 3: Enemy(x,America) -> Hostile(x)
        for fact in facts:
            if (fact[0] == "Enemy" and
                fact[2] == "America"):

                new_facts.add(("Hostile", fact[1]))

        # Rule 4: American(x) AND Weapon(y)
        # AND Sells(x,y,z) AND Hostile(z)
        # -> Criminal(x)

        for f1 in facts:
            for f2 in facts:
                for f3 in facts:
                    for f4 in facts:

                        if (f1[0] == "American" and
                            f2[0] == "Weapon" and
                            f3[0] == "Sells" and
                            f4[0] == "Hostile" and
                            f1[1] == f3[1] and
                            f2[1] == f3[2] and
                            f4[1] == f3[3]):

                            new_facts.add(
                                ("Criminal", f1[1])
                            )

        # Check whether new facts are generated
        if new_facts.issubset(facts):
            break

        facts.update(new_facts)

        # Display newly inferred facts
        print("New Facts:", new_facts)

    # Check the goal
    if ("Criminal", "Robert") in facts:
        print("\nGoal Proved: Robert is Criminal")
    else:
        print("\nGoal Not Proved")


# Execute Forward Chaining
forward_chaining(facts)

