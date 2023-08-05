# GrowattRequestsAsync

Python package to pull PV data from undocumented Growatt API.  
This package uses httpx to make async (non-blocking) HTTP requests.  
GrowattRequestsAsync offers you a quick way to monitor your Growatt systems without having to use Growatt's app. 
It can be easily integrated into your projects (like Home Assistant applications) if you wish to support Growatt and offer your users the ability to monitor and control their Growatt systems.

## Quick Example

```python
import asyncio
import growattRequestsAsync


async def main():
    client = growattRequestsAsync.GrowattRequests(user_agent_randomness=True)
    await client.login("XXXXXXXXXX", "XXXXXXXXXX")
    

if __name__ == "__main__":
    asyncio.run(main())
```

### GrowattRequests Methods

`login(user, pass)` Log into the growatt API. Once logged in a session is created which is necessary in order to send further requests.

`get_plant_list(user_id)` Get a list of plants owned by user.

`get_plant_details(plant_id, timespan, date)` Get details of a specific plant for a given date and over a given timespan (days or months).

`get_plant_info(plant_id)` Get info of a specific plant.

`get_plant_settings(plant_id)` Get the current settings for a specific plant. Growatt API also has an update_plant_settings endpoint which will be added later to this library.

`get_device_list(plant_id)` Get a list of devices (of all types) in a specific plant.

`get_storage_energy_overview(plant_id, storage_device_sn)` Get high-level power generation info for a specific storage device in a specific plant ("Generation overview" page in ShinePhone app).

`get_storage_params(storage_device_sn)` Get information on a storage device.

`get_storage_details(storage_device_sn)` Get detailed data on storage device.

`get_inverter_data(inverter_sn, date)` Get basic information for a specific PV inverter on a specific date.

`get_inverter_details(inverter_sn)` Get detailed information on a specific PV inverter.

`get_dashboard_data(plant_id, timespan, date)` Get "dashboard" values for a specific plant during a specific timespan and for a specific date. 

`get_tlx_data(tlx_inverter_sn, date)` Get basic information about a specific TLX inverter at a specific date (defaults to today).

`get_tlx_details(tlx_inverter_sn)` Get detailed data for a specific TLX inverter.

`get_mix_info(mix_inverter_sn, plant_id=None)` Get high-level information about a specific MIX inverter including daily and overall total information.

`get_mix_today_total(mix_inverter_sn, plant_id)` Get daily and overall total information for a specific MIX inverter.

`get_mix_status(mix_inverter_sn, plant_id)` Get instantaneous (current) values for a specific MIX inverter.

`get_mix_details(mix_inverter_sn, plant_id, timespan, date)` Get detailed information for a specific MIX inverter during a specific timespan (in hours, days, or months) starting from a specific date (defaults to today).


### GrowattRequests Variables

`SERVER_URL` The growatt server URL (default: "https://server.growatt.com/")

`DEFAULT_USER_AGENT` The user-agent set in the header of requests to the Growatt server (can be changed through GrowattRequests() constructor).

## Note

The Growatt API endpoints used in this library were extracted by reverse engineering the Growatt Android app, and they might be changed by Growatt at any time without notice.
