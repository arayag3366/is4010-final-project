from crane_game import *

# Testing to make sure each prize is placed in the prizes array
def test_read_prize_data_file():
    sample_data = """Animal: Turtle
Sound: Weh!
Artist: Joan G. Stark (Spunk)
Color: 38;2;89;196;51
TURTLE IMAGE

Animal: Mouse
Sound: Squeak, squeak!
Artist: Joan G. Stark (Spunk)
Color: 38;2;158;158;158
MOUSE IMAGE

"""

    prizes = read_prize_data(sample_data)
    assert len(prizes) == 2

# Testing to make sure the data in the prizes array is correct
def test_read_prize_data_values():
    sample_data = """Animal: Cat
Sound: Meow!
Artist: Sarah Kearsley
Color: 38;2;255;121;0
   |\\\\---/|
   | ,_, |
    \\\\_`_/-..----.
 ___/ `   ' ,""+ \\ 
(__...'   __\\    |`.___.';
  (_,...'(_,.`__)/'.....+

"""

    prizes = read_prize_data(sample_data)
    cat = prizes[0]

    assert cat.name == "Cat"
    assert cat.sound == "Meow!"
    assert cat.artist == "Sarah Kearsley"
    assert cat.color == "38;2;255;121;0"
    assert "   |\\\\---/|" in cat.appearance

# Testing to make sure the count can be increased
def test_increase_count():
    result = increase_count(2)
    assert result == 3

# Testing to make sure the count can be reset
def test_reset_count():
    result = reset_count(4)
    assert result == 0

# Testing to make sure the claw location based on user inputs is correct
def test_get_claw_location():
    result = get_claw_location('aaadddaaddada')
    assert result == -1