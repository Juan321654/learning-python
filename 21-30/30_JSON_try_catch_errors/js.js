facebook_posts = [
  { Likes: 21, Comments: 2 },
  { Likes: 13, Comments: 2, Shares: 1 },
  { Likes: 33, Comments: 8, Shares: 3 },
  { Comments: 4, Shares: 2 },
  { Comments: 1, Shares: 1 },
  { Likes: 19, Comments: 3 },
];

total_likes = 0;

for (let key of facebook_posts) {
  if (!key["Likes"]) continue;
  total_likes += key["Likes"];
}

console.log(total_likes); // 86