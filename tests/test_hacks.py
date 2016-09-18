from hack_all_the_seqs import hack_what


def test_hackmethod_with_arg():
    assert hack_what("all the seqs") == "all the seqs"

def test_hackmethod_without_arg():
    assert hack_what() == "Hack all the Seqs"
