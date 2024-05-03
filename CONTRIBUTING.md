# Contributing to the paper list

We welcome contributions to this list!

The papers are maintained in the `source` branch under the `papers` directory.
The `README.md` file is generated from the papers in the `papers` directory using the python script `generate_markdown.py`.

The structure of the `papers` directory is as follows:

```
papers
├── phenomena-of-interest
│   ├── in-context-learning
│   ├── chain-of-thought
│   ├── hallucination
│   ├── scaling-laws
│   ├── knowledge
│   ├── training-dynamics
│   ├── learning
│   └── other-phenomena
├── representational-capacity
│   ├── what-can-transformer-do
│   └── what-can-transformer-not-do
├── architectural-effectivity
│   ├── layer-normalization
│   └── tokenization
├── training-paradigms
├── mechanistic-engineering
├── miscellanea
└── README.template
```

There is a `papers.csv` file in each directory that contains the metadata for each paper. The metadata includes the title, authors, date, and URL. The `README.template` file contains the template for the README file.

All you need to do is update the `papers.csv` file in the corresponding directory and pull request to the `source` branch. The GitHub Action will automatically generate the `README.md` file in the `main` branch.

Note:

- The papers can be overlapping across different topics. In such cases, the paper can be added to multiple directories.

- The information in the `papers.csv` file should be in the following format:

```csv
Title,Date,Url,Author
```

- The papers will be sorted by date automatically.

---

Here is a very concrete example on how to contribute:

1. Fork the repository.

2. Clone the forked repository to your local machine.

3. Checkout the `source` branch.

4. Add a new paper to the `papers/phenomena-of-interest/learning/papers.csv` like this:

```csv
Title,Date,Url,Author
... # papers already in the file

On the Role of Attention in Prompt-tuning,2023-06-15,https://openreview.net/forum?id=qorOnDor89,"Oymak, Samet; Rawat, Ankit Singh; Soltanolkotabi, Mahdi; Thrampoulidis, Christos"
```

5. Pull request to the `source` branch.

---

If you have any questions, feel free to open an issue or reach out to the maintainers.

Thank you for contributing!