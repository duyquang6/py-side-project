import statsd

c = statsd.StatsClient('localhost', 8125)
c.incr('golang')  # Increment the 'foo' counter.
