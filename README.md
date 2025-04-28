# a2md
Make a mardown file from anything

## Set up

```bash
pip install 'markitdown[all]'
```

Then execute the a2md.py script with the following command:

```bash
python3 a2md.py <input_file or URL>
```

Markdown is output to the standard output. You can redirect it to a file with the following command:

```bash
python3 a2md. py <input_file> > output.md
```

### Note

I copy the a2md.py file as ~/bin/a2md and make it executable with the following command:

```bash
chmod +x ~/bin/a2md
```

Then I can run it from anywhere with the command:

```bash
a2md <input_file or URL>
```

Enjoy!
