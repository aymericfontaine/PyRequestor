from viewmodels.requestor_viewmodel import RequestorViewModel


class Cmd:
    def __init__(self):       
        self.vm = RequestorViewModel()

    def lanchapp(self):
        while True:
            for i in range(len(self.vm.requests)):
                print(str(i) + ' - ' + self.vm.requests[i].label)

            pos: int
            try:
                pos = int(input("Select  request : "))

                if pos < 0 & pos or pos >= len(self.vm.requests):
                    raise
            except:
                print("Invalid request")
                continue

            self.vm.set_request_pos(pos)

            for i in range(len(self.vm.requests[self.vm.request_pos].params)):
                n = input(self.vm.requests[self.vm.request_pos].params[i].label + " (" + self.vm.requests[self.vm.request_pos].params[i].help + ") : ")
                self.vm.set_param(i, n)

            self.vm.exec_request()

            print('Execute request : ' + self.vm.sql)

            print('Columns :')
            print(self.vm.columns)

            print('Results :')
            print(self.vm.results)

            replay: str
            while True:    
                replay = input('Execute other request (y/n) : ')
                if replay != 'y' and replay != 'n':
                    print('Invalid choice')
                    continue
                else:
                    break

            if replay == 'y':
                continue
            else:
                break

        

cmd = Cmd()
cmd.lanchapp()