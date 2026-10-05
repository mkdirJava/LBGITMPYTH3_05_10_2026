import re
import asyncio
import pytest

async def ispostcode_valid(postcode):
     _regex = (r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|" 
                 r"(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z]" 
                 r"[0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]" 
                 r"[A-Za-z]?))))\s?[0-9][A-Za-z]{2})")

     _matches = re.match(_regex, postcode, re.I)
     if _matches:
         return True
     return False

async def check_postcodes():
       return await asyncio.gather(ispostcode_valid("SW1A 2AA"),
                                   ispostcode_valid("GL1 1HU"),
    	     	                   ispostcode_valid("GL2 6HN"),
                                   ispostcode_valid("GL112 6HN"))

@pytest.mark.asyncio
async def test_all_valid():
      outcomes = await check_postcodes()
      assert all(outcomes)
    
@pytest.mark.asyncio
async def test_some_valid():
       outcomes = await check_postcodes()
       assert any(outcomes)

