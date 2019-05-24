# phones-shop

## Urls:

#### Authentication (non-authenticated)

###### /     (landing page)
###### /phones/
###### /accounts/login/ (login)
###### /questions/create/ (create question)
###### /questions/approved/  (answered and approved questions)

#### Authentication (superuser)

##### /phones/brand/       (adding brand)
##### /phones/delete/{pk}/   (can delete any phone)
##### /questions/pending/    (answer and change status of posted questions)
##### /questions/rejected/    (see rejected questions)
##### /                       (update picture for landing page)

#### Authentication (authenticated)

###### /phones/create/
###### /phones/mine/
###### /phones/search/
###### /accounts/profile/edit/{pk}/ (edit profile phonenumber and picture)
###### /accounts/profile/{pk}/  
###### /accounts/password_change/  (password change)
###### /accounts/password_reset/   (reset passwrod)


