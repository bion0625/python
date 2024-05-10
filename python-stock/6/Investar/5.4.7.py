import Analyzer
mk = Analyzer.MarketDB()
result = mk.get_daily_price('삼양홀딩스', '2024-03-27', '2024-03.29')
print(result)