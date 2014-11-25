from mean_sightings import get_sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
    pigrec,pigmean = get_sightings(filename,'Pig')
    assert pigrec == 1, 'Number of recors for Pig is wrong'
    assert pigmean == 4, 'Mean sightings for pig is wrong'

def test_cow_is_correct():
    cowrec,cowmean = get_sightings(filename,'Cow')
    assert cowrec == 2,'Number of records for cow is wrong'
    assert cowmean == 17,'Mean sightings for cow is wrong'

def test_anonymous_is_correct():
	anirec,animean = get_sightings(filename,'NotPresent')
	assert anirec == 0,'Number of anonymous records is wrong'
	assert animean == 0,'Mean for anonymous animal recs is wrong'