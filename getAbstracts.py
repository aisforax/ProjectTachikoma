import os

len_limit = 3000

dir_path = "pdfs/"
all_files = os.listdir(dir_path)
pdf_files = [f for f in all_files if f.startswith("pdf")]

for i,f in enumerate(pdf_files):
    file_path = dir_path + f

    print "processing %s, %d/%d" % (f, i, len(pdf_files))

    tmp_out_file = "tmp_out.txt"
    cmd = "pdftotext %s %s" % (file_path, tmp_out_file)

    os.system(cmd)

    tmp_out = open(tmp_out_file, 'r')

    abstract = ""
    abs_started = False
    mal_formatted = False
    num_lines = 0

    for line in tmp_out.readlines():
        line = line.strip()
        if not abs_started:
            if line == "Abstract":
                abs_started = True
        else:
            if line == "Abstract":
                mal_formatted = True
                break
            elif line == "":
                break
            else:
                abstract += line
                num_lines += 1

    if mal_formatted:
        print "This file might not be formatted correctly."
    elif not abs_started:
        print "This file might not have abstract."
    elif num_lines > len_limit:
        print "This file's abstract is too long."
    else:
        abs_file = open("abstracts/abs%s" % f[3:], 'w')
        abs_file.write(abstract)
        abs_file.close()
        print "... done."

    tmp_out.close()

cmd = "rm %s" % (tmp_out_file)
os.system(cmd)
