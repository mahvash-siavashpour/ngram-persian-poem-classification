<h1>NLP-Persian-Poets</h1>
<h3>How to use</h3>
1. place your test file in /test_set (include persian poems in persian and their known poets as numbers) <br>
(1: ferdowsi, 2: hafez, 3: molavi) <br>
3. run main.py <br>

<h3>How it works</h3>
This code uses some train sets to learn the n-grams (n=1, 2). These train sets each include the poems from a specific poet. Then the code uses these n-grams in a back-off model to predict the poets of each poem. It also provides some accuracy for the model. 

<h3>Results and Conclusion</h3>
The code managed to predict 85% of the poets correctly. <br>
You can see an example here:<br>
<br>3	تا خدایش باز صاف و خوش کند
<br>3	آنکه تیره کرد هم صافش کند
<br>
=> molavi

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/mahvash-siavashpour/NLP-Persian-Poets/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
