"""
The purpose of this script is to take a bunch of filenames and run the document comparison for all the pairs,
storing the outputs in one big file. This big file will then be  manually labeled for use as training data for
the importance
classifier.
"""
import pandas as pd

import compare_pdfs


def main():
    FILENAMES = [
        "/Users/basenko.dv/upwork/bluewave/sample_files/K112226.pdf",
        "/Users/basenko.dv/upwork/bluewave/sample_files/K112422.pdf",
        "/Users/basenko.dv/upwork/bluewave/sample_files/K112844.pdf",
        "/Users/basenko.dv/upwork/bluewave/sample_files/K113500.pdf",
        # "/Users/basenko.dv/upwork/bluewave/sample_files/K120084.pdf",
        # "/Users/basenko.dv/upwork/bluewave/sample_files/K112376.pdf",
        # "/Users/basenko.dv/upwork/bluewave/sample_files/K112205.pdf",
    ]

    all_result_pairs = []
    print(FILENAMES)
    for i in range(len(FILENAMES)):
        for j in range(i, len(FILENAMES)):
            if i == j:
                continue
            fname_a = FILENAMES[i]
            fname_b = FILENAMES[j]

            result = compare_pdfs.compare_pdf_files(
                filenames=[fname_a, fname_b],
                verbose=True,
                methods=None,
                pretty_print=False,
                no_importance=True,
            )
            pairs = result["suspicious_pairs"]
            for pair in pairs:
                pair["block_text"] = pair["block_text"].replace('\n', '\\n')
            all_result_pairs.extend(pairs)

    df = pd.DataFrame(all_result_pairs)

    df["text"] = df["block_text"]
    df.loc[df["block_text"].notnull(), "text"] = df["block_text"]

    df = df[["pages", "type", "length", "text"]]

    df.to_csv("data/pair_output_1.csv", index=False, quoting=1,)


if __name__ == "__main__":
    main()
