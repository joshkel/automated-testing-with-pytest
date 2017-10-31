# What is Automated Testing?

What is automated testing? And how should you do it?

Pretty quickly gets into controversial territory.

For example, Robert C. Martin's - aka Uncle Bob's - take on testing.  I think that Clean Code is one of the best programming books I've read, but I've never really figured out how TDD applies to the work I do - interacting with hardware, making sure that a plot looks right, doing a complex series of math operations and making sure they give the correct result.

And Uncle Bob can be pretty dogmatic.  He compares Test Driven Development - not just automated testing or unit testing, but full-blown Test Driven Development - to doctors washing their hands, and he strongly implies that it's unprofessional to not use it.

Another take - Michael Feathers. Working Effectively with Legacy Code is a _great_ book, lots of good advice in there, and there's a lot of truth to his argument that you need your tests to be so fast that there's no excuse not to run them, and database and file system access works against that.  But, at the end of the day, I'd rather do what works, and I'd rather have some less-than-optional network and file system tests that I can actually write without a lot of headache.

Matthew Wilson is a C++ developer, so he talks about making the compiler work for him, but the same concept applies to making the computer work for us in general.

Wilson explains that a batman is a term from the British Empire, meaning an orderly or personal servant attached to an officer.  More Samwise Gamgee than Batman.

# Some Notes on Terminology

Unit testing - low-level tests that test a single unit, whatever that is.  A single function or procedure, if you're a procedural programmer.  A single class, or a single class's method, if you're an object-oriented programmer.

Integration testing - testing how things are connected together.  Component tests, system tests.  TO DO: Flesh this out.

Automated testing - doing things automatically.  Martin Fowler calls this "self-testing code"

# Further Reading

Various perspectives on automated testing in general, unit testing in particular, and test-driven development.

Some of these are contradictory - what's "best" isn't always cut and dried, so read and study and figure out what makes sense in your context.

# Further Reading

Some books on the topic.  I haven't yet read most of these, but they're ones that I've seen consistently recommended.

_The Clean Coder_ is one I have read. He has a few chapters on test-driven development, acceptance testing, and how different kinds of testing can fit together into your testing strategy.
