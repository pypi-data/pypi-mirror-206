****************************************
Drill-Bits: Handy tools for ML in Python
****************************************

Install
#######
.. code-block:: bash

    pip install drill-bits
    
    
Examples
########
**All type read & write:**

.. code-block:: python

    from drill-bits.io import io_utils
    data = io_utils.omni_load(file_name)
    io_utils.omni_save(file_name, data)

Currently supported extensions including: `.npy`, `.txt`, `.pkl`, `.jpg`, `.png`.

**A decorator saves you from reprocessing:**

.. code-block:: python
	
    import time
	from drill_bits.operation import base_operation
    
    def foo(n):
    	time.sleep(1)
        if n == 1:
        	return 1
        else:
    		return n * foo(n-1)

    opt = BaseOperation(path).get_handle(force_run=False, verbose=True)
    foo_warp = opt(foo)
    print(foo_warp(5))      # it will take 5s to run
    print(foo_warp(5))      # it will finish immediately 
    opt = BaseOperation(path).get_handle(force_run=True, verbose=True)
    foo_warp = opt(foo)
    print(foo_warp(5))      # it will take 5s to run again
