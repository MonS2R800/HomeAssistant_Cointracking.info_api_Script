# HomeAssistant_Cointracking.info_api_script

A short script that passes values ​​from your Cointracking.info account to a sensor in HomeAssistant.

Install

1. Go to you Home Assistant, create a new folder "python_scripts" in the fileeditor. 
/homeassistant/python_scripts

2. In the folder "python_scripts" create a file with a name of your sensor script.
/homeassistant/python_scripts/your_script_name.py

3. Copy the contents of the file "cointracking_api.py" into the file you just created.

4. Now add your api-key und api-secret, that you had creat on Cointracking.info.

5. go to /homeassistant/configuration.yaml and ad the follow entries:

```ruby
python_script:

sensor:
  - platform: command_line
    name: CoinTracking Balance
    command: "python3 /config/python_scripts/your_script_name.py" # change the script name
    value_template: "{{ value.split('account_summary:')[1].strip() }}"
    unit_of_measurement: "EUR"
    scan_interval: 300

From version 2023.8 the synthax has been changed and must now be inserted into the ocnfigurations.yaml as follows.

command_line:
  - sensor:
      name: CoinTracking Balance
      command: "python3 /config/python_scripts/your_script_name.py"
      value_template: "{{ value.split('account_summary:')[1].strip() }}"
      unit_of_measurement: "EUR"
      scan_interval: 300

```
6. Reboot HomeAssistant.

7. Use your new sensor. For example take a dashbord and ad a new manuel card and insert the follow:

```ruby
type: custom:mini-graph-card
entities:
  - sensor.cointracking_balance # change it, if you wish an other name
name: Cointracking Balance
icon: mdi:ethereum
fill: true
state: true
line_width: 1
hours_to_show: 48
points_per_hour: 12
show:
  average: false
  extrema: true
hour24: true
color_thresholds:
  - value: 1000
    color: '#ff0000'
  - value: 2500
    color: '#d35e00'
  - value: 5000
    color: '#FFFF00'
  - value: 10000
    color: '#FFFF00'
  - value: 15000
    color: '#29ff29'
```

