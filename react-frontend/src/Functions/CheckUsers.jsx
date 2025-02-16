const CheckUsers = (value, group ,users) => {
  let flag = true
  let i = 0
  
  while (flag && i < users.length) {
    switch (group) {
      case 'username':
        if (users[i].USERNAME == value) flag = !flag
        break    
      case 'email':
        if (users[i].EMAIL == value) flag = !flag
        break    
    }
      i++;
  }

  return flag
}

export default CheckUsers