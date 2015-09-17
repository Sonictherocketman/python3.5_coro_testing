Testing Python 3.5's various concurrency methods
================================================

A little suite of tests for gauging the speed of various Python concurrency
methods.

This suite tests:

- CPU Bound operations
- I/O Bound operations
- A mix of CPU and I/O operations

Each of the tests contains 5 parts:

- Sequential execution (for comparison).
- Multiprocessing pool execution (classical Python multiprocessing)
- Multithreading pool execution (classical Python threading)
- Python 3.5 async Coroutines (using a multiprocessing pool)
- Python 3.5 async Coroutines (using a threading pool)

Test it yourself
---------------


    git clone https://github.com/Sonictherocketman/python3.5_coro_testing
    cd python3.5_coro_testing
    bash run.sh


Results
-------

*Retina Macbook Pro (2014, 13")*

<table>
    <th>
        <td>Type</td>
        <td>Test</td>
        <td>Time</td>
    </th>
    <tr>
        <td>CPU Bound</td>
        <td>Serial</td>
        <td>7.804</td>
    </tr>
    <tr>
        <td></td>
        <td>Coro Multi</td>
        <td>4.739s</td>
    </tr>
        <td></td>
        <td>Coro Thread</td>
        <td>8.221s</td>
    </tr>
    <tr>
        <td></td>
        <td>Multiprocess</td>
        <td>4.488s</td>
    </tr>
    <tr>
        <td></td>
        <td>Threading</td>
        <td>8.251s</td>
    </tr>
    
    <tr>
        <td>I/O Bound</td>
        <td>Serial</td>
        <td>1.924s</td>
    </tr>
    <tr>
        <td></td>
        <td>Coro Multi</td>
        <td>0.951s</td>
    </tr>
        <td></td>
        <td>Coro Thread</td>
        <td>1.97s</td>
    </tr>
    <tr>
        <td></td>
        <td>Multiprocess</td>
        <td>1.320s</td>
    </tr>
    <tr>
        <td></td>
        <td>Threading</td>
        <td>1.807s</td>
    </tr>
    
    <tr>
        <td>Mixed I/O and CPU</td>
        <td>Serial</td>
        <td>4.789s</td>
    </tr>
    <tr>
        <td></td>
        <td>Coro Multi</td>
        <td>13.574s</td>
    </tr>
        <td></td>
        <td>Coro Thread</td>
        <td>7.724s</td>
    </tr>
    <tr>
        <td></td>
        <td>Multiprocess</td>
        <td>4.513s</td>
    </tr>
    <tr>
        <td></td>
        <td>Threading</td>
        <td>4.976s</td>
    </tr>
</table>
