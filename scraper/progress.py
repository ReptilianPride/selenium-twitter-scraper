import sys


class Progress:
    def __init__(self, current, total) -> None:
        self.current = current
        self.total = total
        pass

    def print_progress(self,last_tweet_time, current, waiting, retry_cnt, no_tweets_limit) -> None:
        self.current = current
        progress = current / self.total
        bar_length = 40
        progress_bar = (
            "["
            + "=" * int(bar_length * progress)
            + "-" * (bar_length - int(bar_length * progress))
            + "]"
        )
        if no_tweets_limit:
            if waiting:
                sys.stdout.write(
                    "\rTweets scraped : {} - waiting to counter rate limit {}/15 tries".format(
                        current, retry_cnt
                    )
                )
            else:
                sys.stdout.write(
                    "\rTweets scraped : {} & T : 16:27                                      ".format(
                        current,last_tweet_time[11:16]
                    )
                )
        else:
            if waiting:
                sys.stdout.write(
                    "\rProgress: [{:<40}] {:.2%} {} of {} - waiting to counter rate limit {}/15 tries".format(
                        progress_bar, progress, current, self.total, retry_cnt
                    )
                )
            else:
                sys.stdout.write(
                    "\rProgress: [{:<40}] {:.2%} {} of {}                                                  ".format(
                        progress_bar, progress, current, self.total
                    )
                )
        sys.stdout.flush()
