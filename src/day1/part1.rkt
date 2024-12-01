#lang racket

;; reding files
;;https://www.reddit.com/r/Racket/comments/8bosc3/how_to_read_file_line_by_line_fast/
(define (next-line-it file)
  (let ((line (read-line file 'any)))
    (unless (eof-object? line)
      (displayln line)
      (next-line-it file))))

(call-with-input-file "input.txt" next-line-it)