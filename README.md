# Gecho Bang

Free And OpenSourced Audible Alternative with AI powered TTS

### Summary of planning:
1. Create a book shelf with uploaded Books.
2. Make it S3 Compatible.
3. Upload the Book to S3/minio
4. Extract the book content from the pdf.
5. In batch save the content of the books into the S3/Minio.
6. Now goto separate page.
7. When press select a book and press read aloud.
8. Web site will call the S3 and get the chapter texts
	1. Will send the data to Local Installation of the LLM running with exposed API for tts
	2. Will return the `mp3` and S3 url.
9. Web Player will play the chapter.
	1. Once Completed it will mark as completed or will resume from the duration stopped.


### Tech Stack:

1. React
2. FastAPI
3. Minio
4. LLM
5. Docker
6. TTS API

### Task list:

### MVP Version 1.0
- [ ] Create a book shelf with uploaded Books.
- [ ] Make it S3 Compatible.
- [ ] Upload the Book to S3/minio
- [ ] Extract the book content from the pdf.
- [ ] In batch save the content of the books into the S3/Minio.
- [ ] Now goto separate page.
- [ ] When press select a book and press read aloud.
- [ ] Web site will call the S3 and get the chapter texts
  - [ ] Will send the data to Local Installation of the LLM running with exposed API for tts
  - [ ] Will return the `mp3` and S3 url.
- [ ] Web Player will play the chapter.
  - [ ] Once Completed it will mark as completed or will resume from the duration stopped.

### MVP Version 1.1
- [ ] Add the Next JS for SSR
- [ ] Add the User Authentication
- [ ] Add the User Profile
- [ ] Add the User Book Shelf
- [ ] Add the User Book Progress
- [ ] Add the User Book Recommendation
- [ ] Add the User Book Rating
- [ ] Add the User Book Review
- [ ] Add the User Book Comment
- [ ] Add the User Book Sharing
- [ ] Add the User Book Highlight
- [ ] Add the User Book Note
- [ ] Add the User Book Bookmark
- [ ] Add the User Book Search
- [ ] Add the User Book Filter


### MVP Version 1.2
- [ ] Dockerize the Application
- [ ] Add the Kubernetes for Deployment


### MVP Version 1.3
- [ ] Add the Theme Customization
