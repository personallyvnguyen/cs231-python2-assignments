# problem1.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Assignment: Counting on Classes


import re



class Locator():
    '''
    Represents a SRL or a Simplified Resource Locator.
    A SRL contains a kind, location, and resource.
    '''

    @staticmethod
    def is_valid_srl(srl: str) -> bool:
        'Checks if srl is valid using regex'

        regex = r'^[a-z]+:\/{2}([a-zA-Z0-9]+\.)+[a-zA-Z0-9]+(\/[a-zA-Z0-9]+)*$'

        if (re.search(regex, srl) == None):
            return False
        else:
            return True


    def __init__(self, srl: str) -> None:
        'Initializes the class variables'

        if (Locator.is_valid_srl(srl)):
            self._srl = srl
            self._kind = re.search(r'^[a-z]+(?=:\/{2})', srl).group()
            self._location = re.search(
                r'([a-zA-Z0-9]+\.)+[a-zA-Z0-9]+', 
                srl).group()
            self._resource = re.search(r'(\/[a-zA-Z0-9]+)*$', srl).group()
        else:
            raise ValueError


    def srl(self) -> str:
        'Returns the entire SRL'
        return self._srl
    

    def kind(self) -> str:
        "Returns the locator's kind"
        return self._kind

    
    def location(self) -> str:
        "Returns a string representing the locator's location"
        return self._location


    def location_parts(self) -> list[str]:
        '''
        Returns a list of strings representing the parts of a 
        locator's "location"
        '''
        return re.findall(r'\w', self._location)


    def resource(self) -> str:
        "Returns the locator's resource"
        return self._resource


    def resource_parts(self) -> list[str]:
        '''
        Returns a list of strings representing the parts of a 
        locator's "resource"
        '''
        return re.findall(r'\w', self._resource)


    def parent(self) -> 'Locator':
        '''
        Returns a new Locator object where the last resource part has 
        been removed
        '''

        if (len(self.resource_parts()) == 0):
            return Locator(self._srl)
        else:
            rIndex = self._srl.rfind('/')
            return Locator(self._srl[:rIndex])


    def within(self, resource_part: str) -> 'Locator':
        '''
        Returns a new Locator object where the given resource part is 
        appended to the end of the SRL
        '''
        return Locator(self._srl + f'/{resource_part}')



def test_locator_class() -> None:
    'Test Check for the Locator class'

    print('Test Check for Locator class')
    print('-'*30)
    srl = 'w://x.y.z/a/b/c'
    locator = Locator(srl)

    assert locator.srl() == srl, f'FAILED: {locator.srl()} != {srl}'
    print(f'PASSED: {locator.srl()} == {srl}')

    assert locator.kind() == 'w', f'FAILED: {locator.kind()} != w'
    print(f'PASSED: {locator.kind()} == w')

    assert locator.location() == 'x.y.z'
    print(f'PASSED: {locator.location()} == x.y.z')

    assert locator.location_parts() == ['x', 'y', 'z']
    print(f"PASSED: {locator.location_parts()} == ['x', 'y', 'z']")

    assert locator.resource() == '/a/b/c'
    print(f'PASSED: {locator.resource()} == /a/b/c')

    assert locator.resource_parts() == ['a', 'b', 'c']
    print(f"PASSED: {locator.resource_parts()} == ['a', 'b', 'c']")

    parent = locator.parent()
    print('\nTesting parent() function:')
    assert parent.srl() == 'w://x.y.z/a/b'
    print(f'PASSED: {parent.srl()} == w://x.y.z/a/b')

    within = locator.within('d')
    print('\nTesting within() function:')
    assert within.srl() == 'w://x.y.z/a/b/c/d'
    print(f'PASSED: {within.srl()} == w://x.y.z/a/b/c/d')

    print('\nTest Check fully passed.')



if __name__ == '__main__':
    test_locator_class()

