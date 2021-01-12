# Load modules


```python
import sample_annn_pkg as sap
```

# Samples

## sample001


```python
sap.func02()
```

    success!!
    poyo
    

## sample002


```python
# load csv
df0 = sap.datasets.load_sample_data0()
df0
```

    load sample data0
    file format: csv
    sample pandas.DataFrame:
       col1  col2  col3
    0     1     2     3
    1     4     5     6
    2     7     8     9
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



## sample003


```python
# load excel
df1 = sap.datasets.load_sample_data1()
df1
```

    load sample data1
    file format: excel
    sample pandas.DataFrame:
       col4  col5  col6
    0  hoge    10    11
    1  fuga    12    13
    2  poyo    14    15
    3  piyo    16    17
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col4</th>
      <th>col5</th>
      <th>col6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>hoge</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>fuga</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>poyo</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>3</th>
      <td>piyo</td>
      <td>16</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>


