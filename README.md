Binner - Quick And Dirty bin allocation
==========================================================

binner is a quick way to find the best bin sizes for
your items. You give it a set of bins and items, select
an algorithm and it will return you the best fit.

It is for 3 Dimensional space, supports an API
and is a working draft. All work has been experimental 
and has yet to be tested for real case scenarios

Why its something you should use
-------------------------------------------------------

A lot of bin packing apis are paid. This one is free,
It is lightweight, speedy and able to perform basic
bin packing needs.

Algorithms:

Finding Smallest Bin -- Given a set of bins and items
find the smallest bin with enough space for "as" much 
as items as possible

Multiple Bin Packing -- Get the items fit into the provided
set of bins using as much as space as possible 

Single Bin Packing -- Try to fit as many items into one bin as
possible


Example Usage:

running through CLI

```
binner-cli --bins '[{ "title": "test", "w": 100000, "h": 10000, "d": 100, "weight": 20, "id": 1, "max_weight": 1000 }, { "title": "test", "w": 100000, "h": 10000, "d": 100, "weight": 20, "id": 1, "max_weight": 1000 }]' --items '[{ "title": "test", "w": 50, "h": 50, "d": 50, "q": 2, "weight": 200, "id":202 }, { "title": "test", "w": 50, "h": 50, "d": 100, "weight": 20, "id": 2, "max_weight": 1000 }]' --algorithm "multi"
2016-11-25 18:18:11,815 Running algorithm multi
2016-11-25 18:18:11,815 Entering Algorithm MULTI
2016-11-25 18:18:11,815 Packing Bin #2ab4c8a1-d331-43e4-95dc-cfd1833204e0
2016-11-25 18:18:11,816 adding a box at: x: 0, mx: 50, y: 0, my: 50, z: 0, mz: 100
2016-11-25 18:18:11,817 adding a box at: x: 50, mx: 100, y: 0, my: 50, z: 0, mz: 50
2016-11-25 18:18:11,817 Packing Bin #734dbad7-1573-45c9-a409-c613c88c674a
{'packed': [{'bin': {'h': 10000, 'initial': {'h': 10000, 'd': 100, 'w': 100000}, 'd': 100, 'w': 100000, 'id': '2ab4c8a1-d331-43e4-95dc-cfd1833204e0'}, 'slots': [{'min_x': 0, 'min_y': 0, 'min_z': 0, 'item': {'h': 50, 'id': '4a1f4c67-0d0c-448a-a437-814e03c196cf', 'w': 50, 'd': 100}, 'max_z': 100, 'id': 'eed820cf-78ed-420d-bea6-6c41d9af45f2', 'max_x': 50, 'max_y': 50}, {'min_x': 50, 'min_y': 0, 'min_z': 0, 'item': {'h': 50, 'id': 'd4c183d5-40bc-472b-9bac-df1000516107', 'w': 50, 'd': 50}, 'max_z': 50, 'id': '41d8d2f3-0ed6-4c17-86de-72aa0301b30b', 'max_x': 100, 'max_y': 50}]}, {'bin': {'h': 10000, 'initial': {'h': 10000, 'd': 100, 'w': 100000}, 'd': 100, 'w': 100000, 'id': '734dbad7-1573-45c9-a409-c613c88c674a'}, 'slots': []}], 'lost': []}
````

	
only one box filled. given the size

```
binner-cli --algorithm single --bins '[{"w": 1000, "h": 1000, "d": 1000, "id": "Testing Binner Bin"}]' --items '[{"w": 500, "h": 200, "d": 100, "id": "Testing Binner Item"}, {"w": 100, "h": 100, "d": 200, "id": "Testing Binner Item 2"}]'
2016-11-25 18:20:47,577 Running algorithm single
2016-11-25 18:20:47,577 Entering algorithm SINGLE
2016-11-25 18:20:47,577 Trying to allocate items for bin: ebf38305-cf3a-4a74-b10f-4a0ecccf7dce
2016-11-25 18:20:47,578 adding a box at: x: 0, mx: 500, y: 0, my: 500, z: 0, mz: 100
2016-11-25 18:20:47,586 adding a box at: x: 500, mx: 600, y: 0, my: 100, z: 0, mz: 200
2016-11-25 18:20:47,587 Trying to allocate items for bin: ebf38305-cf3a-4a74-b10f-4a0ecccf7dce
2016-11-25 18:20:47,596 adding a box at: x: 0, mx: 500, y: 0, my: 500, z: 100, mz: 200
2016-11-25 18:20:47,609 adding a box at: x: 600, mx: 700, y: 0, my: 100, z: 0, mz: 200
{'packed': [{'bin': {'h': 1000, 'initial': {'h': 1000, 'd': 1000, 'w': 1000}, 'd': 1000, 'w': 1000, 'id': 'ebf38305-cf3a-4a74-b10f-4a0ecccf7dce'}, 'slots': [{'min_x': 0, 'min_y': 0, 'min_z': 0, 'item': {'h': 200, 'id': '27faac95-a76f-44e2-843a-8b0603ae4da7', 'w': 500, 'd': 100}, 'max_z': 100, 'id': '359d3784-b45a-4d5b-a631-2b2d2116840b', 'max_x': 500, 'max_y': 200}, {'min_x': 500, 'min_y': 0, 'min_z': 0, 'item': {'h': 100, 'id': 'f5206e2d-3314-4aa0-8901-891a5166934b', 'w': 100, 'd': 200}, 'max_z': 200, 'id': 'c8549991-02f9-4c7f-b987-072d3dcc00b6', 'max_x': 600, 'max_y': 100}, {'min_x': 0, 'min_y': 0, 'min_z': 100, 'item': {'h': 200, 'id': '27faac95-a76f-44e2-843a-8b0603ae4da7', 'w': 500, 'd': 100}, 'max_z': 200, 'id': '6a7fdf35-ade0-408d-8c9b-f14888b76826', 'max_x': 500, 'max_y': 200}, {'min_x': 600, 'min_y': 0, 'min_z': 0, 'item': {'h': 100, 'id': 'f5206e2d-3314-4aa0-8901-891a5166934b', 'w': 100, 'd': 200}, 'max_z': 200, 'id': 'e27356a2-47e9-4532-98dc-fc40c27ff98b', 'max_x': 700, 'max_y': 100}]}, {'bin': {'h': 1000, 'initial': {'h': 1000, 'd': 1000, 'w': 1000}, 'd': 1000, 'w': 1000, 'id': 'ebf38305-cf3a-4a74-b10f-4a0ecccf7dce'}, 'slots': [{'min_x': 0, 'min_y': 0, 'min_z': 0, 'item': {'h': 200, 'id': '27faac95-a76f-44e2-843a-8b0603ae4da7', 'w': 500, 'd': 100}, 'max_z': 100, 'id': '359d3784-b45a-4d5b-a631-2b2d2116840b', 'max_x': 500, 'max_y': 200}, {'min_x': 500, 'min_y': 0, 'min_z': 0, 'item': {'h': 100, 'id': 'f5206e2d-3314-4aa0-8901-891a5166934b', 'w': 100, 'd': 200}, 'max_z': 200, 'id': 'c8549991-02f9-4c7f-b987-072d3dcc00b6', 'max_x': 600, 'max_y': 100}, {'min_x': 0, 'min_y': 0, 'min_z': 100, 'item': {'h': 200, 'id': '27faac95-a76f-44e2-843a-8b0603ae4da7', 'w': 500, 'd': 100}, 'max_z': 200, 'id': '6a7fdf35-ade0-408d-8c9b-f14888b76826', 'max_x': 500, 'max_y': 200}, {'min_x': 600, 'min_y': 0, 'min_z': 0, 'item': {'h': 100, 'id': 'f5206e2d-3314-4aa0-8901-891a5166934b', 'w': 100, 'd': 200}, 'max_z': 200, 'id': 'e27356a2-47e9-4532-98dc-fc40c27ff98b', 'max_x': 700, 'max_y': 100}]}], 'lost': []}
```

Unit testing
-------------------------------------------------------------------

unit tests are available in ./unit.py. These demonstrate
some use case scenarios. 


Want to help
-------------------------------------------------------------------

If you like 3d geometery and have ideas for this project and feel
these services should not be paid for, contact me any time at [matrix.nad@gmail.com]
