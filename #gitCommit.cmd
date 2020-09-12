set path=%path%;"C:\Programs\Git\bin"
call #git commit --allow-empty -a -m "%1"
call #git push
