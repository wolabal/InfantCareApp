import unittest
import re

# 문자열에서 숫자만 구별하여 int 타입으로 변환하여 반환
def convertStringToNumber(_number):
    number = re.sub('[^0-9]','', _number)
    return int(number)

# 총수를 idx로 나눠서 해당되는 페이지의 인덱스 값을 반환
# 나머지가 있을 경우에는 +1 없을 경우에는 0
# 삼항 연산자는 파이썬 버젼 2.5+ 부터 사용 가능
def getCalculateIndex(totalCount, idx=10):
    _indexCount = (totalCount // idx) + (1 if totalCount % idx > 0 else 0)
    return _indexCount


class InfantCareApptests(unittest.TestCase):
    def test_숫자변환(self):
        _count = '12,000'
        print(convertStringToNumber(_count))

    def test_인덱스_계산(self):
        _count = '12,001'
        print(getCalculateIndex(convertStringToNumber(_count)))

if __name__ == '__main__':
    unittest.main()