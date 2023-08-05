<h1 align="center">
  gyrate
</h1>

<p align="center">create simple yet beautiful code spinners </p>

## warning
🧪 this is meant to be a more featured version of [halo](https://github.com/manrajgrover/halo)
<br> ⚠️ no features have been added yet, so just use halo for the minute !!

## installation

```shell
$ pip install gyrate
```

## examples

```py
from gyrate import Spinner

spinner = Spinner(text='Loading', spinner='dots')
spinner.start()

# Run time consuming work here
# You can also change properties for spinner as and when you want

spinner.stop()
```

Alternatively, you can use halo with Python's `with` statement:

```py
from gyrate import Spinner

with Spinner(text='Loading', spinner='dots'):
    # Run time consuming work here
```

