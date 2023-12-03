# HomeAssistant_Cointracking.info_api_script

A short script that passes values ​​from your Cointracking.info account to a sensor in HomeAssistant.

Install

1. Go to you Home Assistant, create a new folder "python_scripts" in the fileeditor. 
/homeassistant/python_scripts

2. In the folder "python_script" create a file with a name of your sensor.
/homeassistant/python_scripts/your_sensor_name.py

3. Copy the contents of the file "cointracking_api.py" into the file you just created.

4. go to /homeassistant/configuration.yaml and ad the follow entries:

python_script:

sensor:
  - platform: command_line
    name: CoinTracking API
    command: "python3 /config/python_scripts/cointracking_api/your_sensor_name.py" # change the sensor name
    value_template: "{{ value.split('account_summary:')[1].strip() }}"
    unit_of_measurement: "EUR"
    scan_interval: 300

5. reboot HomeAssistant

6. Use your new sensor. For example take a dashbord and ad a new manuel card and insert the follow:

type: custom:mini-graph-card
entities:
  - sensor.cointracking_api
name: Cointracking Balance
icon: mdi:ethereum
fill: true
state: true
line_width: 2
hours_to_show: 72
points_per_hour: 12
show:
  average: false
  extrema: true
hour24: true
color_thresholds:
  - value: 11000
    color: '#ff0000'
  - value: 11500
    color: '#d35e00'
  - value: 12000
    color: '#FFFF00'
  - value: 12500
    color: '#FFFF00'
  - value: 13544
    color: '#29ff29'

