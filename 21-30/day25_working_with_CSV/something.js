let obj = [
  {id: 1, name: 'juan'},
  {id: 1, name: 'tom'},
  {id: 2, name: 'felix'},
  {id: 3, name: 'jon'},
]

for (let user of obj) {
  if (user.id == 1) console.log(user)
}