employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
print('\n'.join(list(filter(lambda x:x[0]=="J", employees))))