def FizzBuzz(var):

  #変数varが、3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」を出力
  if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz", end = "")

  #変数varが、3の倍数の場合は「Fizz」を出力
  elif var % 3 == 0:
    print("Fizz", end = "")
  
  #変数varが、5の倍数の場合は「Buzz」を出力
  elif var % 5 == 0:
    print("Buzz", end = "")

  #上記のどの場合にも該当しない場合は、変数varの値を出力
  else:
    print(var)

  print("")

var = 15
FizzBuzz(var)
