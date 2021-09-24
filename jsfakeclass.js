function user(id, username) {
  let user = {}
  user.id = id
  user.user = username

  function callName(name) {
    return `hi ${name}`
  }

  return {
    user,
    hasName: username,
    callName: callName
  }
}

let user_1 = user(1, "Juan")
console.log(user_1)