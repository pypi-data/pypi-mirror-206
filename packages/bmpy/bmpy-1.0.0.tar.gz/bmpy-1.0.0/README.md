![bmbanner](https://user-images.githubusercontent.com/63975446/232277969-c4fd1424-55ac-4005-8856-18ccbe57ba90.png)

# Bounty Meter PY

Bounty Meter is a command-line utility tool designed for bug bounty hunters to define their bounty target for a year, maintain and keep record of their bounties on a monthly basis, and track their progress throughout the year. With Bounty Meter, you can add and subtract bounties, view your total bounties earned this year, and display an interactive stats card to visualize your progress.

## Getting Started

### Prerequisites

Bounty Meter PY is built using Python scripting language and requires the following tools to be installed on your system:
Bounty Meter is built using Python scripting language and requires the following tools to be installed on your system:

- Python3
- progress (pip install progress)

### Installation

Via PyPi:
```
pip install bmpy
```

### Usage

[ + ] To initialize Bounty Meter and set your bounty target for the year, run the following command:
```
bmpy init bounty_target username
```

Replace `bounty_target` with your desired bounty target for the year and `username` with your hacking alias.

[ + ] To add a new bounty amount to a specified month, run the following command:
```
bmpy add month_name bounty_amount
```

Replace `month_name` with the name of the month (e.g. January, February, etc.) and `bounty_amount` with the amount of the bounty you wish to add to that particluar month.

[ + ] To remove a specified bounty amount from a specified month, run the following command:
```
bmpy sub month_name bounty_amount
```

Replace `month_name` with the name of the month (e.g. January, February, etc.) and `bounty_amount` with the amount of the bounty you want to remove.

[ + ] To display total bounty earned in a particular month, run the following command:
```
bmpy monthly month_name
```
Replace `month_name` with the name of the month (e.g. January, February, etc.) 

[ + ] To display total bounty earned the current year, run the following command:
```
bmpy total
```

[ + ] To display an interactive stats card that shows your progress throughout the year, run the following command:
```
bmpy stats
```

If you want to make the `bmpy stats` command your banner in the terminal, you can add the ```bmpy stats``` command to your `.bashrc` or `.zshrc` file.

## Screnshots
![bmusage](https://user-images.githubusercontent.com/63975446/232277645-5c7f4d74-f1a5-4afc-b91d-1001108576db.png)
![bmmonthly](https://user-images.githubusercontent.com/63975446/232277651-e35d6ed4-b555-49e0-a68c-766a15f450fa.png)
![bmstatscard](https://user-images.githubusercontent.com/63975446/232277657-7d01f347-d39a-4406-9ad2-abba053c55b5.png)

## License

Bounty Meter is licensed under the [MIT License](https://github.com/<username>/<repo>/blob/main/LICENSE).

## Contributing

If you would like to contribute to Bounty Meter, please feel free to fork the repository, make your changes, and submit a pull request. 











