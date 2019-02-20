d = {
    'Rishav' : {'MATH' : 79 , 'Chemistry' : 75 , 'Physics' : 76 },
    'Rupam' : {'MATH' : 80 , 'Chemistry' : 38 , 'Physics' : 95  },
    'Rupesh' : {'MATH' : 95 , 'Chemistry' : 95 , 'Physics' : 90  }
}

print(d)

print(sorted(d, key = lambda item : d.get(item).get('Physics'),reverse=True))