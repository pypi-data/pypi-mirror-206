import sys
import pygraphviz as pgv


# for rich colored printing
from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

console = Console(theme=custom_theme)

transition_function_tmpl = (
    "def {}(input_: str) -> bool:\n"
    "    \"\"\"please implement this function\"\"\"\n"
)

output_function_tmpl = (
    "def {}(input_: str) -> str:\n"
    "    \"\"\"please implement this function\"\"\"\n"
)

class Graph(pgv.AGraph):
    def __init__(self, input_: str):
        """ input_ can be a file name or a dot graph specification"""
        super(Graph, self).__init__(input_)
        #self._graph = pgv.AGraph(input_)

    def get_graph_functions(self) -> list:
        """gets a list of the names of the functions referred to in the
        graph's edges
        """
        fnames_out = []
        for e in self.edges_iter():
            fnames = e.attr['label'].split(':')
            fnames_out.extend(fnames)
        return fnames_out
    def is_implemented(self, fname: str, env={}) -> bool:
        """ checks to see if there is a function named fname"""
        #inspect(env(), all=True)
        if fname in env and callable(env[fname]):
            return True
        return False
    def check_implementation(self, env={}, verbose=False) -> bool:
        if not verbose:
            return any(map(lambda x: self.is_implemented(x, env),
                           self.get_graph_functions()))
        else:
            all_implemented = True
            for e in self.edges_iter():
                transitionfn, outputfn = e.attr['label'].split(':')
                if not self.is_implemented(transitionfn, env):
                    all_implemented = False
                    print(f"# {transitionfn} for {e} is not implemented")
                    print(transition_function_tmpl.format(transitionfn))
                if not self.is_implemented(outputfn, env):
                    all_implemented = False
                    print(f"# {outputfn} for {e} is not implemented")
                    print(output_function_tmpl.format(outputfn))
            return all_implemented
        
                

class FST():
    def __init__(self, graph, start, end, env={}):
        self.graph = graph
        self.start = self.currentstate = start
        self.end = end
        self.is_running = True
        self._env = env

    def __call__(self, input_: str) -> str:
        console.print(f"currentstate: {self.currentstate}", style="info")
        neighbor_edges = self.graph.out_edges(self.currentstate)
        console.print("\tneighbor_edges", style="info")
        valid_edges = []
        output_fns = []
        for e in neighbor_edges:
            console.print("\t\t", e, style="info")
            test_fn, out_fn = e.attr['label'].split(":")
            console.print("\t\t", test_fn, out_fn, style="info")
            if self._env[test_fn](input_):
                valid_edges.append(e)
                output_fns.append(out_fn)
        console.print("\tthere are " + str(len(valid_edges)) + " valid next states",
                      style="info")
        console.print("\t\t", valid_edges,
                      style="info")

        
        if len(valid_edges) == 0:
            print("no valid transitions", file=sys.stderr)
            exit(-1)
        
        # we will pick the first True test function
        self.currentstate = valid_edges[0][1]
        console.print(f"currentstate {self.currentstate}", style="info")
        return self._env[output_fns[0]](input_)

    def run(self) -> None:
        agent_output = self("") # prime the agent because it needs input to start
        console.print(agent_output, style="warning")
        user_input = input()
        while(self.is_running):
            agent_output = self(user_input)
            console.print(agent_output, style="warning")
            user_input = input()                                   

