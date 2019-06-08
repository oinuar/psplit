# psplit
Utility that splits big files to smaller ones by matching split points

## Example use case: Huge SQL file with individual INSERTs that you want to parallelize

Split SQL file into smaller ones in every 10,000th `INSERT INTO` statement. Note that you cannot use `csplit` here because INSERTs may contain new lines. `psplit` works smarter that it identifies split points when splits are allowed.
```bash
mkdir -p huge
cd huge
python ../psplit.py "^INSERT INTO" 10000 ../huge.sql
```

Then a bit bash magic to run these inserts in parallel:
```bash
for filename in *.sql
do
    psql < $filename &
    (( ++count % `nproc` == 0)) && wait
done
```

That's it! Your huge SQL is inserted into database in parallel.
