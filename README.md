# plant-monitor
Monitor plants using a Raspberry Pi and Waylay for #growlab.

This implementation is very specific to my setup, but you can get some inspiration.

### Live dashboards:

* [Waylay IO](https://dashboard-io.waylay.io/public?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbmlzYXRpb24iOiI2MDliYTE2MjRlMmEwNzQ4Mzk5YTIzZjkiLCJkYXNoYm9hcmRJZCI6IjYwOWJhYzA4NWEwOTc0NzExODdkODUxMiIsInJlc291cmNlSWQiOiIwMTg0ZDY3ZS01OGExLTQ3NjktYWFjZC03OWRlZjI5YzhjOGEiLCJyb2xlIjoicHVibGljIiwidXNlciI6IjYwOWJhOGQ0NGUyYTA3NWJmZDlhMjNmYyIsImRvbWFpbiI6ImlvLXRlc3Rpbmcud2F5bGF5LmlvIiwidGVuYW50IjoiNjY0MTc4NTctOWY0OS00YTgzLTkzMDctZTEyYWQ1ZmJkYTQ1IiwiaWF0IjoxNjIwODE0ODc0LCJpc3MiOiJ3YXlsYXlEYXNoYm9hcmQifQ.B-XfXh-LUz9uSk62t9yd_C0I-gQyOIbeMLZkbSoEGEE)
* [sandervanhove.com/plant-monitor](https://www.sandervanhove.com/plant-monitor)

### What it does:

1. Measure values
2. Post them to [Waylay IO](https://www.waylay.io/products/waylay-io/product)
3. Snap a picture (if there is enough light)
4. Upload the values and picture to a [github repo](https://github.com/SanderVanhove/plant-monitor-data) that purely holds this data
5. Repeat every 5min
