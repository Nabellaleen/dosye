# TODO

## Fullstack / Backend

- Implement a feature to manage folders
  - Ability to create folders and choose in which folder upload a file
  - Ability to move files from a folder to another folder
- Implement an account management system
  - Authentication system
  - Ability to have multiple users, each viewing their own files
  - Ability to have different roles, with admin who can create normal users
  - Ability to share files publicly, and/or to other users
  - Ability to manage rights on sharing (read, write)
- Display more informations about files : file format, size, ...

## Backend

- Implement tests : unit tests, API tests, Doctests, ...

## Frontend

- Implement `browse` UI in `angular`, like it already exists with `vue`
- Merge `upload` and `browse` UIs to have a "Single Page Application"
- Implement a "Search bar", client side
- Implement "Preview file" widgets for common files (text, images, music, video, ...)

## AI

- Implement an algorithm tagging files automatically depending of their content
  - Do it on text files, image files, ...
  - Allow to send request on dosye API to find files depending on their tags

## DevOp

- Make the project run on AWS
- Add CI
- Proxify with a WSGI server (gunicorn)