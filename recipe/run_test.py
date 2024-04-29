# HACK: from __future__ import annotations must be the first line, but conda build injects print statements. 
#import _run_test
from __future__ import annotations

from google.protobuf.struct_pb2 import ListValue, Struct

print("Tests complete")
