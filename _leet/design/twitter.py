"""
https://leetcode.com/problems/design-twitter/

"""
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #Tracks all users of twitter. Key is the user, value is a "SET" the user follows
        self.users = {} #contains {follwer1:set(followee1, followee2),   follower2:set()}
        
        #Maps users to all tweets they've made. Tweets are a tuple where we track recency of tweet with the
        #tweet counter below, and the actual tweet ID
        self.tweets = {}    #contains list of (tweet_counter, tweetId)
        
        # tweet_counter helps to store "LIST" of tweets in most recent order inside "HEAPQ": useful for dashboard
        # this also means, to display dashboard, we dont have to iterate over all the tweets and sort to most recent
        #Tracks all tweets being made on twitter. Python doesn't have max heap so we use a negative to record.
        #Every time a tweet is made, tweet_counter is decremented. The most recent tweet will be the most
        #negative number we see. If you use a max heap, this would be the greatest number from a positive,
        #but we use negatives since we can't do max heaps
        self.tweet_counter = -1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        #Check if this user exists in our running users and tweets list, since both contains users as keys.
        #If not, just add them with None values for their keys
        if userId not in self.users:
            self.users[userId] = set()
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        #Get list of tweets this user has made. This will be a list of tuples.
        list_of_tweets = self.tweets[userId]
        
        #The tuple consists of tweet counter on twitter itself, and tweetId. We use tweet counter
        #so that we can order tweets from least to most recent to dispaly on our feed.
        new_tweet = (self.tweet_counter, tweetId)
        list_of_tweets.append(new_tweet)
        
        #Assign the updated list to the user in the tweets dictionary, and decrement our running counter
        #by 1 since a new tweet has been made
        self.tweets[userId] = list_of_tweets
        self.tweet_counter -= 1
        
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        #First check to see if the user themselves have made tweets in the tweet dictionary. If so, add to
        #our running heap
        if userId in self.tweets:
            my_tweets = self.tweets[userId]
            for tweet_number, tweet_Id in my_tweets:
                heapq.heappush(heap, (tweet_number, tweet_Id))
        
        #Now check what users this person follows. Add their tweets to our heap too
        if userId in self.users:
            my_followed = self.users[userId]
            for followed in my_followed:
                if followed in self.tweets:
                    their_tweets = self.tweets[followed]
                    for tweet_number, tweet_Id in their_tweets:
                        heapq.heappush(heap, (tweet_number, tweet_Id))
        
        #Our max heap now has all tweets we can have. We just now pop the 10 most recent one's. Since
        #it's a heap, we just keep popping it until it's empty, or if we have our max of 10
        return_list = []

        for i in range(len(heap)):
            if len(return_list) >= 10:
                break
            return_list.append(heapq.heappop(heap)[1])
        return return_list
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        
        #Edge case. User should not follow themselves.
        if followerId == followeeId:
            return
        
        #If the user is already on twitter
        if followerId in self.users:
            #Get the users this person follows. This will be a set
            followed = self.users[followerId]
            #Add the new followee to the set
            followed.add(followeeId)
            #Update the set with the new followee added
            self.users[followerId] = followed
        else:
            #Create the user in the users dictionary with an empty set
            self.users[followerId] = set()
            #Get the set you just created. Will be empty
            followed = self.users[followerId]
            #Add the followee to this set now.
            followed.add(followeeId)
            #Update the set with the new followee added
            self.users[followerId] = followed
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        #First check if the followerId is a user on twitter
        if followerId in self.users:
            #Get the users this person follows. This will be a set
            followed = self.users[followerId]
            #Now check the user actually follows this followee
            if followeeId in followed:
                followed.remove(followeeId)
                #Update the set with the followee deleted
                self.users[followerId] = followed
        else:
            #Create the user in the users dictionary with an empty set. Since nothing to remove, just return after.
            self.users[followerId] = set()


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

'''
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. 
If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')


A priority queue is common use for a heap, and it presents several implementation challenges:
- Sort stability: how do you get two tasks with equal priorities to be returned in the order they were originally added?
- Tuple comparison breaks for (priority, task) pairs if the priorities are equal and the tasks do not have a default comparison order.
- If the priority of a task changes, how do you move it to a new position in the heap?
- Or if a pending task needs to be deleted, how do you find it and remove it from the queue?

A solution to the first two challenges is to store entries as 3-element list including the priority, an entry count, and the task. 
The entry count serves as a tie-breaker so that two tasks with the same priority are returned in the order they were added. 
And since no two entry counts are the same, the tuple comparison will never attempt to directly compare two tasks.



'''