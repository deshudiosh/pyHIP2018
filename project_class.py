class Project:
    name = url = times_to_vote = None

    def __init__(self, lines):
        # find first date in group
        for line in lines:
            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                self.date_start = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find last date in group
        for line in reversed(lines):
            # consider only 'Result accepted' lines as the ones that finish session
            if 'Result accepted by the pool' not in line:
                continue

            date_start = line.find('[')
            date_end = line.find(']')
            if date_start > -1 and date_end > -1:
                self.date_end = datetime.strptime(line[date_start + 1:date_end], '%Y-%m-%d %H:%M:%S')
                break

        # find avg hash rates
        avg = Average()
        for line in lines:
            if 'Totals:' in line:
                avg.add_from_string(line)
        self.hashrate = avg.get()

        self.duration = self.date_end - self.date_start if (self.date_start and self.date_end) else "---"

    def __str__(self):
        return "    ".join([str(v) for v in [self.date_start, self.duration, self.hashrate]])