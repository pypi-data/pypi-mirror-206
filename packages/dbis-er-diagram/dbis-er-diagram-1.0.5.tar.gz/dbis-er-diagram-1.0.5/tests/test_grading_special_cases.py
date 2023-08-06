from erdiagram import ER, grade_submission


def test_renamed_cardinality_1_n():
    solution = ER()
    solution.add_relation({"A": "1"}, "R1", {"B": "n"})
    solution.add_relation({"C": "1"}, "R2", {"D": "n"})
    solution.add_relation({"E": "n"}, "R3", {"F": "n"})
    solution.add_relation({"G": "n"}, "R4", {"H": "m"})
    solution.add_relation({"I": "n"}, "R5", {"J": "1", "K": "1"})
    solution.add_relation({"L": "n"}, "R6", {"M": "1", "N": "m"})
    solution.add_relation({"O": "n"}, "R7", {"P": "1", "Q": "n"})
    solution.add_relation({"R": "n"}, "R8", {"S": "m", "T": "n"})
    solution.add_relation({"U": "n"}, "R9", {"V": "m", "W": "m"})

    submission = ER()
    submission.add_relation({"A": "1"}, "R1", {"B": "n"})
    submission.add_relation({"C": "1"}, "R2", {"D": "m"})
    submission.add_relation({"E": "m"}, "R3", {"F": "m"})
    submission.add_relation({"G": "m"}, "R4", {"H": "n"})
    submission.add_relation({"I": "m"}, "R5", {"J": "1", "K": "1"})
    submission.add_relation({"L": "m"}, "R6", {"M": "1", "N": "n"})
    submission.add_relation({"O": "m"}, "R7", {"P": "1", "Q": "m"})
    submission.add_relation({"R": "m"}, "R8", {"S": "n", "T": "m"})
    submission.add_relation({"U": "m"}, "R9", {"V": "n", "W": "n"})

    score, log = grade_submission(solution, submission)
    assert score == 0


def test_renamed_cardinality_min_max():
    solution = ER()
    solution.add_relation({"A": "(1, 1)"}, "R1", {"B": "(1, n)"})
    solution.add_relation({"C": "(1, 1)"}, "R2", {"D": "(1, n)"})
    solution.add_relation({"E": "(1, n)"}, "R3", {"F": "(1, n)"})
    solution.add_relation({"G": "(1, n)"}, "R4", {"H": "(1, m)"})
    solution.add_relation({"I": "(1, n)"}, "R5", {"J": "(n, m)"})
    solution.add_relation({"L": "(m, n)"}, "R6", {"M": "(1, 1)", "N": "(1, m)"})
    solution.add_relation({"O": "(1, m)"}, "R7", {"P": "(n, m)", "Q": "(1, n)"})
    solution.add_relation({"R": "(1, m)"}, "R8", {"S": "(m, n)", "T": "(1, m)"})
    solution.add_relation({"U": "(n,m)"}, "R9", {"V": "(m, n)", "W": "(m, m)"})
    solution.add_relation({"X": "(n,m) "}, "R10", {"Y": "(m, n)", "Z": "(1, n)"})

    submission = ER()
    submission.add_relation({"A": "(1, 1)"}, "R1", {"B": "(1, n)"})
    submission.add_relation({"C": "(1, 1)"}, "R2", {"D": "(1, m)"})
    submission.add_relation({"E": "(1, m)"}, "R3", {"F": "(1, m)"})
    submission.add_relation({"G": "(1, m)"}, "R4", {"H": "(1, n)"})
    submission.add_relation({"I": "(1, m)"}, "R5", {"J": "(m,n)"})
    submission.add_relation({"L": "(n, m)"}, "R6", {"M": "(1, 1)", "N": "(1, n)"})
    submission.add_relation({"O": "(1, n)"}, "R7", {"P": "(m, n)", "Q": "(1, m)"})
    submission.add_relation({"R": "(1, n)"}, "R8", {"S": "(n,m)", "T": "(1, n)"})
    submission.add_relation({"U": "(m,n) "}, "R9", {"V": "(n, m)", "W": "(n,n)"})
    submission.add_relation({"X": "(m,n)"}, "R10", {"Y": "(n,m)", "Z": "(1, m)"})

    score, log = grade_submission(solution, submission)
    assert score == 0


def test_renamed_cardinality_1_n_incorrect():
    solution = ER()
    solution.add_relation({"A": "m"}, "R1", {"B": "n", "C": "m"})
    submission = ER()
    submission.add_relation({"A": "n"}, "R1", {"B": "m", "C": "m"})

    score, log = grade_submission(solution, submission)
    assert score > 0


def test_renamed_cardinality_min_max_incorrect():
    solution = ER()
    solution.add_relation({"A": "(m, n)"}, "R1", {"B": "(n, m)", "C": "(m, n)"})
    submission = ER()
    submission.add_relation({"A": "(n, m)"}, "R1", {"B": "(m, n)", "C": "(m, n)"})

    score, log = grade_submission(solution, submission)
    assert score > 0
