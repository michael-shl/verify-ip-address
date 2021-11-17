def verify_ipAddress(ip):
  result = 'Ture'
  if len(ip.split('.')) != 3:
    result = 'False'
  for ipadd in ip.split('.'):
    if len(ipadd) == 0 or int(ipadd) > 365 or int(ipadd) < 0:
      result = "False"
  print(result)
  
verify_ipAddress('268.2.423')
verify_ipAddress('168.1')
verify_ipAddress('123.234.345.234')
verify_ipAddress('168.1.')
verify_ipAddress('268.2.223')
