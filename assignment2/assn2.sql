-- 1.
-- frequency(docid, term, count)
-- (a) select: Write a query that is equivalent to the following relational algebra expression.

-- σ10398_txt_earn(frequency)


-- SELECT count(*)
-- FROM(
-- SELECT *
-- FROM frequency
-- WHERE docid='10398_txt_earn'
-- ) x;



-- (b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.
-- πterm(σdocid=10398_txt_earn and count=1(frequency))
-- SELECT count(*)
-- FROM (
-- SELECT term
-- FROM frequency
-- WHERE docid='10398_txt_earn'
-- and count=1
-- ) x;



-- (c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)

-- πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
-- SELECT count(*)
-- FROM (
-- (SELECT term
-- FROM frequency
-- WHERE docid='10398_txt_earn' and count=1)
-- UNION
-- (SELECT term
-- FROM frequency
-- WHERE docid='925_txt_trade' and count=1)
-- ) x;


-- (d) count: Write a SQL statement to count the number of documents containing the word "parliament"

-- SELECT count(*)
-- FROM(
--         SELECT *
--         FROM frequency
--         WHERE term LIKE 'parliament'
-- ) x;

-- (e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. 

-- SELECT DISTINCT count (*)
-- FROM (
--      SELECT docid, term, SUM(count) as total
--      FROM frequency
--      GROUP BY docid
-- )
-- WHERE total > 300;


-- (f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
-- Self-join on docid, count no. rows with both required terms in it

-- SELECT count(*)
--        FROM (
--             SELECT f1.docid, f1.term, f2.term
--             FROM frequency f1
--             INNER JOIN frequency f2
--             ON f1.docid = f2.docid
--             WHERE f1.term LIKE 'transactions' AND f2.term LIKE 'world'
-- );

-- 2. 
-- (g) multiply: Express A X B as a SQL query, referring to the class lecture for hints.
-- What to turn in: On the assignment page, enter the value of the cell (2,3)

-- SELECT val
-- FROM (
--      SELECT A.row_num, B.col_num, SUM(A.value*B.value) as val
--      FROM A,B
--      WHERE A.col_num = B.row_num
--      GROUP BY A.row_num, B.col_num
-- )
-- WHERE row_num = 2 and col_num = 3
-- ;

-- 3.
-- (h) similarity matrix: Write a query to compute the similarity matrix DDT. (Hint: The transpose is trivial -- just join on columns to columns instead of columns to rows.) 

-- What to turn in: On the assignment page, enter the similarity of the two documents '10080_txt_crude' and '17035_txt_earn'.

-- Compute transpose
-- Do matrix multiplication
-- Find similarity between 10080_txt_crude' and '17035_txt_earn'

-- SELECT val
-- FROM (
--      SELECT A.row_num, B.col_num, SUM(A.value*B.value) as val
--      FROM A,B
--      WHERE A.col_num = B.row_num
--      GROUP BY A.row_num, B.col_num
-- )
-- WHERE row_num = 2 and col_num = 3
-- ;

PRAGMA table_info(frequency);
