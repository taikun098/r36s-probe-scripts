import pyfdt.pyfdt as f
import inspect
print("module attrs:", [x for x in dir(f) if not x.startswith('_')])
print("---Fdt---")
print([x for x in dir(f.Fdt) if not x.startswith('_')])
try:
    print("Fdt init:", inspect.signature(f.Fdt.__init__))
except Exception as e:
    print("init err", e)
for name in ['wraparse','Fdt','FdtNode','FdtProperty','FdtPropertyStrings','FdtPropertyWords','FdtPropertyBytes']:
    obj = getattr(f, name, None)
    if obj is not None:
        print(name, ":", [x for x in dir(obj) if not x.startswith('_')])
